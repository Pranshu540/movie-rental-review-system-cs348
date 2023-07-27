import { Component } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';

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
    private router: Router) {}

  onDeleteUser() {

    // this.username = '';
    let userList: any[] = [];
    if (localStorage.getItem('userList')) {
      userList = JSON.parse(localStorage.getItem('userList')!);
    }
    userList = userList.filter(user => user.username !== this.username);
    localStorage.setItem('userList', JSON.stringify(userList));
    

    this._snackBar.open('User deleted successfully', 'Close', {
      duration: 1000,
    });
    localStorage.removeItem(this.username+'-rentals');
    sessionStorage.clear();
    setTimeout(() => {
      this.router.navigate(['login']);
    }, 1000);
  }
}
