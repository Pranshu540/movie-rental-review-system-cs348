import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Movie } from '../components/search/search.component';

@Injectable({
  providedIn: 'root'
})
export class BackendCommunicationService {

  private baseUrl = 'http://localhost:5000/';

  constructor(private http: HttpClient) { }

  signin(username: string, password: string) {
    return this.http.post(`${this.baseUrl}/signin`, {username, password});
  }

  signup(username: string, password: string) {
    return this.http.post(`${this.baseUrl}/signup`, {username, password});
  }

  rentMovie(userId: number, movieId: number) {
    return this.http.post(`${this.baseUrl}/${userId}/rent_movie/${movieId}`, {});
  }

  checkRentals() {
    return this.http.get(`${this.baseUrl}/rentals`);
  }

  createReview(userId: number, movieId: number, rating: number, comment: string) {
    return this.http.post(`${this.baseUrl}/create_review/${userId}/${movieId}`, {rating, comment});
  }

  deleteReview(userId: number, movieId: number) {
    return this.http.delete(`${this.baseUrl}/remove_review/${userId}/${movieId}`);
  }

  editReview(userId: number, movieId: number, rating: number, comment: string) {
    return this.http.put(`${this.baseUrl}/modify_review/${userId}/${movieId}`, {rating, comment});
  }

  getSingleReview(userId: number, movieId: number) {
    return this.http.get(`${this.baseUrl}/check_review/${userId}/${movieId}`);
  }

  // TODO
  getMovieReviews(movieName: string) {
    return this.http.get(`${this.baseUrl}/get_movie_reviews/${movieName}`);
  }

  getUserRentals(userName: string) {
    return this.http.get(`${this.baseUrl}/get_user_rentals/${userName}`);
  }

  getAllReviews() {
    return this.http.get(`${this.baseUrl}/check_all_reviews`);
  }

  deleteUser(userId: number) {
    return this.http.delete(`${this.baseUrl}/delete_user/${userId}`);
  }

  getRecommendedMovies(username: string) {
    return this.http.get(`${this.baseUrl}/username`, {params: {username}});
  }

  filterMovies(title?: string, count?: number, genre?: string): Observable<Movie[]> {
    let params = new HttpParams();
    if (title) params = params.append('title', title);
    if (count) params = params.append('count', count.toString());
    if (genre) params = params.append('genre', genre);

    return this.http.get(`${this.baseUrl}/filter_movie`, {params}) as Observable<Movie[]>
  }
}
