import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';
import { StudentLoginRequest } from './models/StudentLoginRequest';
import { Observable } from 'rxjs';
import { TutorLoginRequest } from './models/TutorLoginRequest';
import { StudentSignupRequest } from './models/StudentSignupRequest';
import { TutorSignupRequest } from './models/TutorSignupRequest';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  
  constructor(private httpManager: httpManager, private cookieService: CookieService, private router: Router) { 
  }

  isAuthenticated() : boolean {
    if(!this.cookieService.check('userId') || !this.cookieService.check('userType'))
    {
      return false;
    }
    return true;
  }

  logout()
  {
    this.cookieService.delete('userId');
    this.cookieService.delete('userType');
    this.router.navigate(['']);
  }

  studentSignup(user: StudentSignupRequest): Observable<number>
  {
    let result = this.httpManager.studentSignup(user);   
    return result;
  }

  tutorSignUp(user: TutorSignupRequest): Observable<number>
  {
    let result = this.httpManager.tutorSignup(user);
    return result;
  }

  studentLogin(request : StudentLoginRequest) : Observable<number>
  {
    let result = this.httpManager.studentLogin(request);
    return result;
  }

  tutorLogin(request : TutorLoginRequest) : Observable<number>
  {
    let result = this.httpManager.tutorLogin(request);
    return result;
  }
}
