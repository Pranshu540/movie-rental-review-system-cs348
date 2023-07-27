import { Injectable } from '@angular/core';
import { Rental } from '../components/rental-view/rental-view.component';
@Injectable({
  providedIn: 'root'
})
export class RentalDataService {

  constructor() { }

  private rentals: Rental[] = [];
  
  getRentals() { 
    const username = sessionStorage.getItem('username');
    this.rentals = localStorage.getItem(username+'-rentals') ? JSON.parse(localStorage.getItem('rentals')!) : [];
    return this.rentals;
  }

  setRentals(rentals: Rental[]) {
    const username = sessionStorage.getItem('username');
    this.rentals = rentals;
    localStorage.setItem(username+'-rentals', JSON.stringify(this.rentals));
  }
}
