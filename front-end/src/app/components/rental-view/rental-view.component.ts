import { Component } from '@angular/core';
import { OnInit } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { RentalDataService } from 'src/app/services/rental-data.service';

export interface Rental {
  movie_name: string,
  rental_start_date: Date,
  rental_end_date: Date
}

@Component({
  selector: 'app-rental-view',
  templateUrl: './rental-view.component.html',
  styleUrls: ['./rental-view.component.scss']
})
export class RentalViewComponent implements OnInit{

  rentals: any[] = []

  constructor(private backendService: BackendCommunicationService, private rentalDataService: RentalDataService){}

  async ngOnInit() {
    this.rentals = this.rentalDataService.getRentals();

    // if (username) this.backendService.getUserRentals(username).subscribe(data => {
    //   
    //   const data_new = data as Rental[];
    //   DATA = data_new;
    // })

  }
  displayedColumns: string[] = ['movie_name', 'rental_start_date', 'rental_end_date'];

  
  

}
