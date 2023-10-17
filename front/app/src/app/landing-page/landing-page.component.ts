import { Component } from '@angular/core';
import { faRightToBracket } from '@fortawesome/free-solid-svg-icons';
import { Router } from '@angular/router';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss']
})
export class LandingPageComponent {
  faRightToBracket = faRightToBracket;

  constructor(private router: Router) { }
  
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




