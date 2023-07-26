import { Component } from '@angular/core';
import { Router } from '@angular/router';

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

  constructor(private router: Router){

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
  submit(formValue: any) {
    console.log(formValue);

    const user = this.userList.find((user) => user.username === formValue.username && user.password === formValue.password);
    const newUser = formValue.newUser === 'Yes';
    if (!user && newUser) {
      this.userList.push({username: formValue.username, password: formValue.password});
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

