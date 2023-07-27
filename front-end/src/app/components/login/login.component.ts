import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { BackendCommunicationService } from 'src/app/services/backend-communication.service';
import { tap } from 'rxjs/operators';

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
  

  submit(formValue: any) {
    console.log(formValue);
    const newUser = formValue.newUser === 'Yes';

    this.backendService.signin(formValue.username, formValue.password).pipe(
      tap((value: any) => {
        alert("user exists? from db: " + value);
        let userExists: boolean = false;
        if (typeof (value) === "boolean") userExists = value;

        if (!userExists && newUser) {
          this.backendService.signup(formValue.username, formValue.password).subscribe(() => {
            this.setSessionData(formValue);
          });
        } else if (!userExists && !newUser) {
          alert('User not found');
        } else if (userExists && newUser) {
          alert('User already exists');
        } else {
          this.setSessionData(formValue);
        }
      })
    ).subscribe();

    // find way to determine if isAdmin from backend
    sessionStorage.setItem('isAdmin', true.toString());
  }



}

