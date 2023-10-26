import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { StudentLoginRequest } from '../models/StudentLoginRequest';
import { TutorLoginRequest } from '../models/TutorLoginRequest';
import { AuthenticationService } from '../authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  isStudent: boolean = true;
  emailNotFound: boolean = false;
  wrongPassword: boolean = false;
  missingFields: boolean = false;

  email: string = '';
  password: string = '';

  constructor(
    private route : ActivatedRoute,
    private router : Router,
    private authenticationService: AuthenticationService) {
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    });
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

      this.authenticationService.studentLogin(request).subscribe(id => {
        this.router.navigate(['/appointments/student', id]);
      });
    }
    else
    {
      let request : TutorLoginRequest = {
        email: this.email,
        password: this.password
      };

      this.authenticationService.tutorLogin(request).subscribe(id => {
        this.router.navigate(['/profile', id]);
      });
    }
  }

}
