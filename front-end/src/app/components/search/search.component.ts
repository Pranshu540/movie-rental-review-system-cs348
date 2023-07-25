// search.component.ts
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { Router } from '@angular/router';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';

interface Movie {
  title: string;
  available: boolean;
  genre?: string;
}

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit {

  constructor(
    private router: Router
  ) {}

  movies: Movie[] = [
    {title: "The Shawshank Redemption", available: true, genre: "Drama"},
    {title: "The Godfather", available: false, genre: "Drama"},
    {title: "The Godfather: Part II", available: false, genre: "Drama"},
    {title: "The Dark Knight", available: false, genre: "Action"},
    {title: "12 Angry Men", available: false, genre: "Drama"},
    {title: "Schindler's List", available: false, genre: "Drama"},
    {title: "The Lord of the Rings: The Return of the King", available: false, genre: "Adventure"},
    {title: "Pulp Fiction", available: false, genre: "Drama"},
    {title: "The Good, the Bad and the Ugly", available: false, genre: "Western"},
    {title: "Fight Club", available: false, genre: "Drama"},
  ];

  movieControl = new FormControl();
  filteredMovies!: Observable<Movie[]>;
  showAvailable: boolean = false;

  ngOnInit() {
    this.filteredMovies = this.movieControl.valueChanges
      .pipe(
        startWith(''),
        map(value => this._filterMovies(value))
      );
  }

  private _filterMovies(value: string): Movie[] {
    let filterValue = '';
  
    if(value) {
      filterValue = value.toLowerCase();
    }
  
    // consider 'showAvailable' when filtering the movies
    let filteredMovies = this.movies.filter(movie => 
      movie.title.toLowerCase().includes(filterValue) && (!this.showAvailable || movie.available)
    );
    // debug
    console.log('Show available:', this.showAvailable);
    console.log('Filtered movies:', filteredMovies);
    return filteredMovies;
  }

  refreshMovies() {
    const currentValue = this.movieControl.value;
    this.movieControl.setValue('a');
    setTimeout(() => this.movieControl.setValue(currentValue), 0);
  }

  optionSelected(event: MatAutocompleteSelectedEvent) {
    const movieTitle = event.option.value;
    this.router.navigate(['movies', movieTitle]);
  }
}