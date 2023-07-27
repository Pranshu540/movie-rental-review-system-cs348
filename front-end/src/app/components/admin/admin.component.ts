import { Component } from '@angular/core';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent {
  username: string = '';

  constructor(private backendService: BackendCommunicationService) {}

  onDeleteUser() {
    if (this.username.trim() === '') {
      
      return;
    }

    this.backendService.deleteUser(this.username).subscribe(
      () => {
        
      },
      (error: any) => {
        // Handle any errors here
        console.error('Error deleting user:', error);
        
      }
    );

    this.username = '';
  }
}
