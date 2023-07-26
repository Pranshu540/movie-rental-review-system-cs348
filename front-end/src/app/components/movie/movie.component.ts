import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { Input } from '@angular/core';
import { SimpleChanges } from '@angular/core';

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

  @Input() movieTitle: string = '';

  constructor(route: ActivatedRoute, private movieService: MovieService) {
    // route.params.subscribe(params => this.selectedMovie.title = params['name']);
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['movieTitle']) {
      console.log('movieTitle changed: ', this.movieTitle);
      this.reloadMovie();
    }
  }

  ngOnInit() {
    
  }
  

}
