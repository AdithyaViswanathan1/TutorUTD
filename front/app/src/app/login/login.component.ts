import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { StudentLoginRequest } from '../models/StudentLoginRequest';
import { TutorLoginRequest } from '../models/TutorLoginRequest';
import { AuthenticationService } from '../authentication.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  isStudent: boolean = true;
  emailNotFound: boolean = false;
  wrongPassword: boolean = false;
  missingFields: boolean = false;

  email: string = '';
  password: string = '';

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

  login(){
    console.log("login");
    //check for missing fields
    if(this.email == '' || this.password == '') {
      this.missingFields = true;
      return;
    }
    else {
      this.missingFields = false;
    }


    if(this.isStudent)
    {
      let request : StudentLoginRequest = {
        email: this.email,
        password: this.password
      };

      this.authenticationService.studentLogin(request).subscribe(response => {
        if(response.enroll_url)
        {
          this.router.navigate(['duo', 'student']);
        }
        if(response.user_id)
        {
          this.cookieService.set('userId', response.user_id.toString());
          this.cookieService.set('userType', 'student');
          this.router.navigate(['/appointments']);
        }
      });
    }
    else
    {
      let request : TutorLoginRequest = {
        email: this.email,
        password: this.password
      };

      this.authenticationService.tutorLogin(request).subscribe(response => {
        if(response.enroll_url)
        {
          this.router.navigate(['duo', 'tutor']);
        }
        if(response.user_id)
        {
          this.cookieService.set('userId', response.user_id.toString());
          this.cookieService.set('userType', 'tutor');
          this.router.navigate(['/profile', response.user_id]);
        }
      });
    }
  }

}
