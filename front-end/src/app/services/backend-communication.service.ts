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
    return this.http.post(`${this.baseUrl}/auth/signin`, {username, password});
  }

  signup(username: string, password: string) {
    return this.http.post(`${this.baseUrl}/auth/signup`, {username, password});
  }

  rentMovie(userId: number, movieId: number) {
    return this.http.post(`${this.baseUrl}/${userId}/rent_movie/${movieId}`, {});
  }

  /*
    returns an array of movie titles the user has rented
    */
  rentMovieByName(username: string, moveieName: string) {
    return this.http.post(`${this.baseUrl}/${username}/rent_movie_by_name/${moveieName}`, {});
  }

  checkRentals() {
    return this.http.get(`${this.baseUrl}/rentals`);
  }


  addReview(username: string, moviename: string, rating: number, comment: string): Observable<any> {
    const url = `${this.baseUrl}/create_review/${username}/${moviename}`;
    return this.http.post(url, { rating, comment });
  }

  deleteReview(username: string, moviename: string): Observable<any> {
    const url = `${this.baseUrl}/delete_review/${username}/${moviename}`;
    return this.http.delete(url);
  }

  editReview(username: string, moviename: string, rating: number, comment: string): Observable<any> {
    const url = `${this.baseUrl}/edit_review/${username}/${moviename}`;
    return this.http.put(url, { rating, comment });
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

  deleteUser(username: string) {
    return this.http.delete(`${this.baseUrl}/delete_user/${username}`);
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
