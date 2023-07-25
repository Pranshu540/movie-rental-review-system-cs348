import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MovieService {
  apiKey = '09906a8ffa24affc69ec6a73c71c97ee';
  tmdbUrl = 'https://api.themoviedb.org/3';
  imageUrl = 'https://image.tmdb.org/t/p/w500';

  constructor(private http: HttpClient) { }

  searchMovies(query: string): Observable<any> {
    const searchUrl = `${this.tmdbUrl}/search/movie?api_key=${this.apiKey}&query=${query}`;
    return this.http.get(searchUrl);
  }

  getPosterUrl(posterPath: string): string {
    return `${this.imageUrl}${posterPath}`;
  }
}
