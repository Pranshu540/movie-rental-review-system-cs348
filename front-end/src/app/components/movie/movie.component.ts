import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { Input } from '@angular/core';
import { SimpleChanges } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { Rental, RentalViewComponent } from '../rental-view/rental-view.component';
import { RentalDataService } from 'src/app/services/rental-data.service';
import { timeout } from 'rxjs';


interface Movie {
  title: string;
  available: boolean;
  genre: string;
  price: string;
  duration: string;
  releaseYear: string;
}

@Component({
  selector: 'app-movie',
  templateUrl: './movie.component.html',
  styleUrls: ['./movie.component.scss']
})
export class MovieComponent implements OnInit {
  selectedMovie: Movie = {} as Movie;

  posterUrl: string = '';

  async reloadMovie() {
    this.posterUrl = await this.movieService.getMovieImage(this.movieTitle);
    console.log(this.posterUrl)
  }

  canRent: boolean = true;

  @Input() movieTitle: string = '';

  constructor(route: ActivatedRoute, 
    private movieService: MovieService,
    private backendService: BackendCommunicationService,
    private rentalDataService: RentalDataService) {
    // route.params.subscribe(params => this.selectedMovie.title = params['name']);
  }

  async ngOnChanges(changes: SimpleChanges) {
    
    if (changes['movieTitle']) {
      const username = localStorage.getItem('username')!;
      console.log('movieTitle changed: ', this.movieTitle);
      await this.reloadMovie();
      if (this.rentalDataService.getRentals().map(rental => rental.movie_name).includes(this.movieTitle)) {
        this.canRent = false;
      }
      this.selectedMovie.title = this.movieTitle;
      this.selectedMovie.genre = this.movieService.movies.filter(movie => movie.title === this.movieTitle)[0].genre;
      this.selectedMovie.price = "9.99";
      if (localStorage.getItem(this.movieTitle+"-runtime")) {
        const minutes = parseInt(localStorage.getItem(this.movieTitle+"-runtime")!);
        // format in hours and minutes
        const formatted_minutes = Math.floor(minutes/60) + 'h' +minutes%60 + ' minutes';
        this.selectedMovie.duration = formatted_minutes;
      }
      if ((localStorage.getItem(this.movieTitle+"-release_date"))) {
        this.selectedMovie.releaseYear = localStorage.getItem(this.movieTitle+"-release_date")!;
        // get everything before first '-'
        this.selectedMovie.releaseYear = this.selectedMovie.releaseYear.split('-')[0];
      }

    }
  }

  ngOnInit() {
    // check currently rented movies
    this.backendService.getUserRentals(localStorage.getItem('username')!).subscribe(
      (data: any) => {
        
        const data_new = data as Rental[];
        if (data_new.map(rental => rental.movie_name).includes(this.movieTitle)) {
          this.canRent = false;
        }
      }
    )
    
  }

  rentMovie() {
    
    // this.backendService.rentMovieByName(localStorage.getItem('username')!, this.movieTitle).subscribe(
    //   (value: any) => {
    //     
    //   }
    // )
    
    const username = localStorage.getItem('username')!;
    


    const rentals = this.rentalDataService.getRentals();
    rentals.push({
      movie_name: this.movieTitle,
      rental_start_date: new Date(),
      rental_end_date: new Date('August 8, 2023 03:24:00')
    })
    
    this.rentalDataService.setRentals(rentals);
    let balance = localStorage.getItem('balance')!;
    balance = (parseInt(balance) - 9.99).toString();
    localStorage.setItem('balance', balance);
    
    this.canRent = false;
  }
  

}
