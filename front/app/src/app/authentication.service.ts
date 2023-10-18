import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';
import { SignUpRequest } from './models/SignUpRequest';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  manager: httpManager;
  
  constructor(httpManager: httpManager) { 
    this.manager = httpManager;
  }

  studentSignUp(user: SignUpRequest): boolean 
  {
    this.manager.signUp(user);   
    return true;
  }

  tutorSignUp(user: SignUpRequest): boolean
  {
    this.manager.signUp(user);
    return true;
  }

}
