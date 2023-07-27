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
    if (localStorage.getItem('userList')) {

      const userList = JSON.parse(localStorage.getItem('userList')!);
      
      if (userList.length > 0) {
        this.userList = userList;
      }
    }
    if (sessionStorage.getItem('username') && sessionStorage.getItem('password')) {
      console.log('Already logged in');
      this.router.navigate(['home']);
    }
  }

  private setSessionData(formValue: any) {
    sessionStorage.setItem('username', formValue.username);
    sessionStorage.setItem('password', formValue.password);

    
    
    this.router.navigate(['home']);
  }
  
  
  userList: User[] = [{username: 'nj', password: 'nj'}]; // TODO: replace with API call
  async submit(formValue: any) {
    
    console.log(formValue);
    let user = this.userList.find(user => user.username === formValue.username && user.password === formValue.password);

    const newUser = formValue.newUser === 'Yes';
    if (!user && newUser) {
      this.userList.push({username: formValue.username, password: formValue.password});
      localStorage.setItem('userList', JSON.stringify(this.userList));
      this.setSessionData(formValue);
    } else if (!user && !newUser) {
      
    } else if (user && newUser) {
      
    } else {
      this.setSessionData(formValue);
    }
    if (formValue.username === "nj") {
      sessionStorage.setItem('isAdmin', 'true')
    }
  }
}

