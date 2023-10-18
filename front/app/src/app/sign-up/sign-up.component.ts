import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service';
import { SignUpRequest } from '../models/SignUpRequest';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent {
  isStudent: boolean = true;
  missingFields: boolean = false;
  badPassword: boolean = false;
  noMatch: boolean = false;
  emailExists: boolean = false;


  fName: string = '';
  lName: string = '';
  email: string = '';
  password: string = '';
  cPassword: string = '';

  constructor(
    private route : ActivatedRoute,
    private router : Router,
    private authenticationService: AuthenticationService) {
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    });
  }

  signUp() {
    console.log('sign up');

    //check for missing fields
    if(this.fName == '' || this.lName == '' || this.email == '' || this.password == '' || this.cPassword == '') {
      this.missingFields = true;
      return;
    }
    else {
      this.missingFields = false;
    }

    //check for bad password
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(this.password)) {
      this.badPassword = true;
      return;
    }
    else {
      this.badPassword = false;
    }

    // check if passwords match
    if (this.password !== this.cPassword) {
      this.noMatch = true;
      return;
    }
    else {
      this.noMatch = false;
    }


    //call login service for user
    if(this.isStudent)
    {
      let user : SignUpRequest = {
        email: this.email,
        password: this.password,
        firstName: this.fName,
        lastName: this.lName,
        isStudent: true
      }

      this.authenticationService.studentSignUp(user);
    }
    else
    {
      let user : SignUpRequest = {
        email: this.email,
        password: this.password,
        firstName: this.fName,
        lastName: this.lName,
        isStudent: false
      }
    }

    if(this.isStudent)
    {
      this.router.navigate(['/appointments', 'student']);
    }
    else
    {
      this.router.navigate(['/profile/0']); //TODO: grab created id
    }
  }

  devCheatNav()
  {
    if(this.isStudent)
    {
      this.router.navigate(['/appointments', 'student']);
    }
    else
    {
      this.router.navigate(['/profile/0']);
    }
  }
}
