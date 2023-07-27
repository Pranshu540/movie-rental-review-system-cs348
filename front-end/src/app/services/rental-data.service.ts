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
    if (localStorage.getItem(username+'-rentals')) {
      this.rentals = JSON.parse(localStorage.getItem(username+'-rentals')!);
      
    }
    return this.rentals;
  }

  clearUserRentals() {
    const username = sessionStorage.getItem('username');
    localStorage.removeItem(username+'-rentals');
    this.rentals = [];
  }

  setRentals(rentals: Rental[]) {
    const username = sessionStorage.getItem('username');
    this.rentals = localStorage.getItem(username+'-rentals') ? JSON.parse(localStorage.getItem('rentals')!) : [];
    localStorage.setItem(username+'-rentals', JSON.stringify(rentals));
  }
}
