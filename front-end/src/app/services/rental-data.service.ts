import { Injectable } from '@angular/core';
import { Rental } from '../components/rental-view/rental-view.component';
@Injectable({
  providedIn: 'root'
})
export class RentalDataService {

  constructor() { }

  private rentals: Rental[] = [];
  
  getRentals() { 
    this.rentals = localStorage.getItem('rentals') ? JSON.parse(localStorage.getItem('rentals')!) : [];
    return this.rentals;
  }

  setRentals(rentals: Rental[]) {
    this.rentals = rentals;
    localStorage.setItem('rentals', JSON.stringify(this.rentals));
  }
}
