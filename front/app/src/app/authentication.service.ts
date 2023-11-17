import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';
import { StudentLoginRequest } from './models/StudentLoginRequest';
import { Observable } from 'rxjs';
import { TutorLoginRequest } from './models/TutorLoginRequest';
import { StudentSignupRequest } from './models/StudentSignupRequest';
import { TutorSignupRequest } from './models/TutorSignupRequest';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { LoginResponse } from './models/LoginResponse';
import { RegisterResponse } from './models/RegisterResponse';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  
  private duoQrUrl: string = '';

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

  studentSignup(user: StudentSignupRequest): Observable<RegisterResponse>
  {
    let result = this.httpManager.studentSignup(user);   
    return result;
  }

  tutorSignUp(user: TutorSignupRequest): Observable<RegisterResponse>
  {
    let result = this.httpManager.tutorSignup(user);   
    return result;
  }

  studentLogin(request : StudentLoginRequest) : Observable<LoginResponse>
  {
    let result = this.httpManager.studentLogin(request);
    return result;
  }

  tutorLogin(request : TutorLoginRequest) : Observable<LoginResponse>
  {
    let result = this.httpManager.tutorLogin(request);
    return result;
  }
}
