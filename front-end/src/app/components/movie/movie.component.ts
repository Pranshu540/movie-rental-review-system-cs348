import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { Input } from '@angular/core';
import { SimpleChanges } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { Rental, RentalViewComponent } from '../rental-view/rental-view.component';
import { RentalDataService } from 'src/app/services/rental-data.service';


interface Movie {
  title: string;
  available: boolean;
  genre: string;
  price: number;
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

  ngOnChanges(changes: SimpleChanges) {
    if (changes['movieTitle']) {
      console.log('movieTitle changed: ', this.movieTitle);
      this.reloadMovie();
      if (localStorage.getItem(this.movieTitle+'-available') === 'false') {
        this.canRent = false;
      }
      this.selectedMovie.available = this.canRent;
      this.selectedMovie.title = this.movieTitle;
      this.selectedMovie.genre = 'Action';
      this.selectedMovie.price = 5;
      if (sessionStorage.getItem(this.movieTitle+"-runtime")) {
        const minutes = parseInt(sessionStorage.getItem(this.movieTitle+"-runtime")!);
        // format in hours and minutes
        const formatted_minutes = Math.floor(minutes/60) + 'h' +minutes%60 + ' minutes';
        this.selectedMovie.duration = formatted_minutes;

      }
      if (sessionStorage.getItem(this.movieTitle+"-release_date")) {
        this.selectedMovie.releaseYear = sessionStorage.getItem(this.movieTitle+"-release_date")!;
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
    // let rentals: any = localStorage.getItem(username+'-Rentals');
    // if (rentals) {
    //   rentals = JSON.parse(rentals) as Rental[];
    //   rentals.push({
    //     movie_name: this.movieTitle,
    //     rental_start_date: new Date(),
    //     rental_end_date: new Date('August 8, 2023 03:24:00')
    //   })
    //   localStorage.setItem(username+'-Rentals', JSON.stringify(rentals));
    // } else {
    //   rentals = JSON.stringify([{
    //     movie_name: this.movieTitle,
    //     rental_start_date: new Date(),
    //     rental_end_date: new Date('August 8, 2023 03:24:00')
    //   }])
    //   localStorage.setItem(username+'-Rentals', rentals);
    //   
    // }
    
    this.canRent = false;
    localStorage.setItem(this.movieTitle+'-available', 'false');
  }
  

}
