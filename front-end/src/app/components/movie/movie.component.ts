import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { Input } from '@angular/core';
import { SimpleChanges } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { Rental } from '../rental-view/rental-view.component';


interface Movie {
  title: string;
  available: boolean;
  genre: string;
  price: number;
  duration: string;
  releaseYear: number;
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
    private backendService: BackendCommunicationService) {
    // route.params.subscribe(params => this.selectedMovie.title = params['name']);
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['movieTitle']) {
      console.log('movieTitle changed: ', this.movieTitle);
      this.reloadMovie();
    }
  }

  ngOnInit() {
    // check currently rented movies
    this.backendService.getUserRentals(sessionStorage.getItem('username')!).subscribe(
      (data: any) => {
        alert("User rentals from backend: "+JSON.stringify(data))
        const data_new = data as Rental[];
        if (data_new.map(rental => rental.movie_name).includes(this.movieTitle)) {
          this.canRent = false;
        }
      }
    )
    
  }

  rentMovie() {
    alert('Renting movie: ' + this.movieTitle);
    this.backendService.rentMovieByName(sessionStorage.getItem('username')!, this.movieTitle).subscribe(
      (value: any) => {
        alert("rent movie from backend: "+JSON.stringify(value));
      }
    )
    this.canRent = false;
  }
  

}
