import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { Input } from '@angular/core';

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

  @Input() movieTitle: string = '';

  constructor(route: ActivatedRoute, private movieService: MovieService) {
    // route.params.subscribe(params => this.selectedMovie.title = params['name']);
  }

  ngOnInit() {
    if (this.movieTitle != '') {
      this.movieService.searchMovies(this.movieTitle).subscribe(
        data => {
          console.log('Movie data:', data);
          if (data.results.length > 0) {
            this.posterUrl = this.movieService.getPosterUrl(data.results[0].poster_path);
          }
        },
        error => {
          console.error('Error:', error);
        }
      );
    }
    }
  

}
