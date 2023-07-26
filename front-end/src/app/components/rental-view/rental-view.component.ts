import { Component } from '@angular/core';

export interface Rental {
  movie_name: string,
  rental_start_date: Date,
  rental_end_date: Date
}

// fake data
const DATA: Rental[] = [
  {movie_name: 'The Dark Knight', rental_start_date: new Date(), rental_end_date: new Date('August 8, 2023 03:24:00')},
  {movie_name: 'The Shawshank Redemption', rental_start_date: new Date(), rental_end_date: new Date('August 8, 2023 03:24:00')},
]

@Component({
  selector: 'app-rental-view',
  templateUrl: './rental-view.component.html',
  styleUrls: ['./rental-view.component.scss']
})
export class RentalViewComponent {
  displayedColumns: string[] = ['movie_name', 'rental_start_date', 'rental_end_date'];
  dataSource = DATA;

  

}
