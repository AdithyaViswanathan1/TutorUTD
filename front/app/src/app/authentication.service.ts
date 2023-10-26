import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';
import { StudentLoginRequest } from './models/StudentLoginRequest';
import { Observable } from 'rxjs';
import { TutorLoginRequest } from './models/TutorLoginRequest';
import { StudentSignupRequest } from './models/StudentSignupRequest';
import { TutorSignupRequest } from './models/TutorSignupRequest';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  manager: httpManager;
  
  constructor(httpManager: httpManager) { 
    this.manager = httpManager;
  }

  studentSignup(user: StudentSignupRequest): Observable<number>
  {
    let result = this.manager.studentSignup(user);   
    return result;
  }

  tutorSignUp(user: TutorSignupRequest): Observable<number>
  {
    let result = this.manager.tutorSignup(user);
    return result;
  }

  studentLogin(request : StudentLoginRequest) : Observable<number>
  {
    let result = this.manager.studentLogin(request);
    return result;
  }

  tutorLogin(request : TutorLoginRequest) : Observable<number>
  {
    let result = this.manager.tutorLogin(request);
    return result;
  }

}
