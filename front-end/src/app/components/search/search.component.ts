// search.component.ts
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { Router } from '@angular/router';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { switchMap } from 'rxjs/operators';
import { from } from 'rxjs';

export interface Movie {
  title: string;
  available: boolean;
  genre: string;
}

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
})
export class SearchComponent implements OnInit {

  constructor(
    private router: Router,
    private backendService: BackendCommunicationService
  ) {}

  movieTitle: string = '';

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

  // Array for distinct genres
  genres: string[] = [
    "Action",
    "Adventure",
    "Animation",
    "Biography",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Family",
    "Fantasy",
    "Film-Noir",
    "Game-Show",
    "History",
    "Horror",
    "Music",
    "Musical",
    "Mystery",
    "News",
    "Reality-TV",
    "Romance",
    "Sci-Fi",
    "Sport",
    "Talk-Show",
    "Thriller",
    "War",
    "Western",
  ];

  // Model for selected genre
  selectedGenre: string | undefined;

  ngOnInit() {
    this.filteredMovies = this.movieControl.valueChanges.pipe(
      startWith(''),
      switchMap(value => this._filterMovies(value))
    );
  }


  private _filterMovies(value: string): Observable<Movie[]> {
    let filterValue = '';

    if (value) {
        filterValue = value.toLowerCase();
    }

    // consider 'showAvailable' and 'selectedGenre' when filtering the movies
    let filteredMovies = from(this.backendService.filterMovies(filterValue, undefined, this.selectedGenre))

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
    this.movieTitle = event.option.value;
  }
}
