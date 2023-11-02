import { Component, OnInit, inject } from '@angular/core';
import { faRightToBracket } from '@fortawesome/free-solid-svg-icons';
import { Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss']
})
export class LandingPageComponent implements OnInit{
  faRightToBracket = faRightToBracket;

  constructor(private router: Router,
    private authService: AuthenticationService,
    private cookieService: CookieService) { }
  
  ngOnInit(): void {
    if(this.authService.isAuthenticated())
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
  
  toLoginPage(student : boolean) {
    if(student)
    {
      this.router.navigate(['/login', 'student']);
    }
    else
    {
      this.router.navigate(['/login', 'tutor']);
    }
  }

  toSignUpPage(student : boolean) {
    if(student)
    {
      this.router.navigate(['/signup', 'student']);
    }
    else
    {
      this.router.navigate(['/signup', 'tutor']);
    }
  }
}




