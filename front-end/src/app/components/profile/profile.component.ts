import { Component } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { RentalDataService } from 'src/app/services/rental-data.service';
import { Review } from '../review/review.component';
import { MovieService } from 'src/app/services/movie.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent {

  username: string = sessionStorage.getItem('username')!;

  balance: string = localStorage.getItem('balance')!;

  constructor(
    private _snackBar: MatSnackBar,
    private router: Router,
    private rentalService: RentalDataService,
    private movieService: MovieService) {}

    onDeleteUser() {

    this.movieService.movies.forEach((movie: any) => {
      movie = movie.title;
      localStorage.removeItem(this.username+" reviewed "+movie)
      // delete review if it exists
      const review: string | null = localStorage.getItem(movie!+'-reviews');

      if (review) {
        let review_data: Review[] = JSON.parse(review);

        review_data = review_data.filter((review: Review) => review.username !== this.username);
        localStorage.setItem(movie!+'-reviews', JSON.stringify(review_data));
      }
    });

    // this.username = '';
    let userList: any[] = [];
    if (localStorage.getItem('userList')) {
      userList = JSON.parse(localStorage.getItem('userList')!);
    }
    userList = userList.filter(user => user.username !== this.username);
    localStorage.setItem('userList', JSON.stringify(userList));
    
    this.rentalService.clearUserRentals();
    this._snackBar.open('User deleted successfully', 'Close', {
      duration: 1000,
    });

    sessionStorage.removeItem('username');
    sessionStorage.removeItem('password');
    
    setTimeout(() => {
      this.router.navigate(['login']);
    }, 1000);
    
  }
}
