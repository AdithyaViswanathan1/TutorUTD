import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service';
import { StudentSignupRequest } from '../models/StudentSignupRequest';
import { TutorSignupRequest } from '../models/TutorSignupRequest';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent implements OnInit {
  isStudent: boolean = true;
  missingFields: boolean = false;
  badPassword: boolean = false;
  noMatch: boolean = false;
  emailExists: boolean = false;
  loading: boolean = false;

  fName: string = '';
  lName: string = '';
  email: string = '';
  password: string = '';
  cPassword: string = '';

  constructor(
    private route : ActivatedRoute,
    private router : Router,
    private authenticationService: AuthenticationService,
    private cookieService: CookieService) {
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    });
  }

  ngOnInit(): void {
    if(this.authenticationService.isAuthenticated())
    {
      let userType = this.cookieService.get('userType');
      if(userType == 'student')
      {
        this.router.navigate(['/appointments']);
      }
      else if(userType == 'tutor')
      {
        this.router.navigate(['/profile', this.cookieService.get('userId')]);
      }
    }
  }

  signUp() {
    //check for missing fields
    if(this.fName == '' || this.lName == '' || this.email == '' || this.password == '' || this.cPassword == '') {
      this.missingFields = true;
      return;
    }
    else {
      this.missingFields = false;
    }

    //check for bad password
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$/; // 8 characters, 1 uppercase, 1 number, 1 special character
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

    this.loading = true;

    //call auth service for user
    if(this.isStudent)
    {
      let request : StudentSignupRequest = {
        email: this.email,
        password: this.password,
        full_name: this.fName + ' ' + this.lName
      };

      this.authenticationService.studentSignup(request).subscribe(z =>
        {
          this.loading = false;
          this.cookieService.set('duoQrUrl', z.enroll_url);
          this.router.navigate(['/duo', 'student']);
        });
    }
    else
    {
      let request : TutorSignupRequest = {
        email: this.email,
        password: this.password,
        full_name: this.fName + ' ' + this.lName
      };

      this.authenticationService.tutorSignUp(request).subscribe(z =>
        {
          this.loading = false;
          this.cookieService.set('duoQrUrl', z.enroll_url);
          this.router.navigate(['/duo', 'tutor']);
        });
    }
  }
}
