import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { LoginRequest } from './models/LoginRequest';
import { SignUpRequest } from './models/SignUpRequest';


@Injectable({
    providedIn: 'root'
})
export class Manager {
    backendUrl : string = 'https://example.com/api';

    constructor(private http: HttpClient) {}

    signUp(user: SignUpRequest) 
    {
        //return this.http.post(this.backendUrl, user);
    }

    login(user: LoginRequest)
    {
        //return this.http.post(this.backendUrl, user);
    }
}
