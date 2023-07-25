import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs';
import { map, startWith, } from 'rxjs/operators';
import { OnInit } from '@angular/core';


@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit {
  movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Godfather: Part II",
    "The Dark Knight",
    "12 Angry Men",
    "Schindler's List",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "Fight Club"
  ];

  movieControl = new FormControl();
  filteredMovies!: Observable<string[]>;

  ngOnInit() {
    this.filteredMovies = this.movieControl.valueChanges
      .pipe(
        startWith(''),
        map(value => this._filterMovies(value))
      );
  }

  private _filterMovies(value: string): string[] {
    const filterValue = value.toLowerCase();

    return this.movies.filter(movie => movie.toLowerCase().includes(filterValue));
  }
}
