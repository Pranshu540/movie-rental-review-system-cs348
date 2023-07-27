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

    if (sessionStorage.getItem('username') && sessionStorage.getItem('password')) {
      console.log('Already logged in');
      this.router.navigate(['home']);
    }
  }

  private setSessionData(formValue: any) {
    sessionStorage.setItem('username', formValue.username);
    sessionStorage.setItem('password', formValue.password);

    alert('Login successful');
    this.router.navigate(['home']);
  }
  
  
  userList: User[] = [{username: 'nj', password: 'nj'}]; // TODO: replace with API call
  async submit(formValue: any) {
    console.log(formValue);
    let user = true;
    await this.backendService.signin(formValue.username, formValue.password).subscribe(
      (value: any) => {
        alert("user exists? from db: "+value)
        if (typeof(value) === "boolean") user = value
      }
    )
    const newUser = formValue.newUser === 'Yes';
    if (!user && newUser) {
      this.backendService.signup(formValue.username, formValue.password);
      this.setSessionData(formValue);
    } else if (!user && !newUser) {
      alert('User not found');
    } else if (user && newUser) {
      alert('User already exists');
    } else {
      this.setSessionData(formValue);
    }
  }
}

