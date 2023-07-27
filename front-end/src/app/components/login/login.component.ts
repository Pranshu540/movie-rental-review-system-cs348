import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';

interface User {
  username: string;
  password: string;
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  constructor(private router: Router, private backendService: BackendCommunicationService){

    if (localStorage.getItem('username') && localStorage.getItem('password')) {
      console.log('Already logged in');
      this.router.navigate(['home']);
    }
  }

  private setSessionData(formValue: any) {
    localStorage.setItem('username', formValue.username);
    localStorage.setItem('password', formValue.password);

    
    this.router.navigate(['home']);
  }
  
  
  userList: User[] = [{username: 'nj', password: 'nj'}]; // TODO: replace with API call
  async submit(formValue: any) {
    console.log(formValue);
    let user = this.userList.find(user => user.username === formValue.username && user.password === formValue.password);

    const newUser = formValue.newUser === 'Yes';
    if (!user && newUser) {
      this.userList.push({username: formValue.username, password: formValue.password});
      this.setSessionData(formValue);
    } else if (!user && !newUser) {
      
    } else if (user && newUser) {
      
    } else {
      this.setSessionData(formValue);
    }
  }
}

