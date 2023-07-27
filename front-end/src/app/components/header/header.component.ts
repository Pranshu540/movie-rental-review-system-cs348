import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent {
  constructor(private router: Router) {}
  isAdmin: boolean = sessionStorage.getItem('isAdmin') === 'true';
  navigate(location: string) {
    
    this.router.navigate([location]);
  }

}
