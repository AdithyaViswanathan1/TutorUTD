import { Injectable } from '@angular/core';
import { Manager } from './manager';
import { SignUpRequest } from './models/SignUpRequest';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  constructor(manager: Manager) { }

  studentSignUp(username: string, password: string): boolean 
  {
    user: SignUpRequest = {
      email: username,
      password: password,
      firstName: '',
      lastName: '',
      isStudent: true
    }
    
    return false;
  }

}
