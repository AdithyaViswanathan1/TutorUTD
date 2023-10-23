import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

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
    private router : Router) {
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

    // submit form
    console.log('submit form');

    if(this.isStudent)
    {
      this.router.navigate(['/appointments', 'student']);
    }
    else
    {
      this.router.navigate(['/profile']);
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
      this.router.navigate(['/profile']);
    }
  }
}
