import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { switchMap, map } from 'rxjs/operators';
import { of } from 'rxjs';
import { Movie } from '../components/search/search.component';


@Injectable({
  providedIn: 'root'
})
export class MovieService {
  apiKey = '09906a8ffa24affc69ec6a73c71c97ee';
  tmdbUrl = 'https://api.themoviedb.org/3';
  imageUrl = 'https://image.tmdb.org/t/p/w500';

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

  constructor(private http: HttpClient) {
    this.searchMovies("Barbie")
   }

  searchById(id: number): Observable<any> {
    const searchUrl = `${this.tmdbUrl}/movie/${id}?api_key=${this.apiKey}`;
    return this.http.get(searchUrl);
  }

  searchMovies(query: string): Observable<any> {
    const searchUrl = `${this.tmdbUrl}/search/movie?api_key=${this.apiKey}&query=${query}`;
  
    return this.http.get(searchUrl).pipe(
      map((data: any) => {
        if (data.results) {
          const result: any = data.results[0];
          localStorage.setItem(query+"-release_date", result.release_date);
          return result.id;
        }
        return null;
      }),
      switchMap(id => {
        if (id) {
          return this.searchById(id);
        }
        return of(null);
      }),
      map((data: any) => {
        if (data) {
          console.log(JSON.stringify(data));
          localStorage.setItem(query+"-runtime", data.runtime);
        }
        return data;
      })
    );
  }

  getPosterUrl(posterPath: string): string {
    return `${this.imageUrl}${posterPath}`;
  }

  async getMovieImage(movieTitle: string) {
    if (movieTitle != '') {
      try {
        const data = await this.searchMovies(movieTitle).toPromise();
  
        console.log('Movie data:', data);
  
        if (data) {
          return this.getPosterUrl(data.poster_path);
        } else {
          return '';
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  
    return '';
  }
  

}
