import { Component } from '@angular/core';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent {
  username: string = sessionStorage.getItem('username')!;

  balance: string = localStorage.getItem('balance')!;
}
