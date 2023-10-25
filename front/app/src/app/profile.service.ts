import { Injectable } from '@angular/core';
import { Tutor } from './models/Tutor';
import { Observable, of } from 'rxjs';
import { httpManager } from './httpManager';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  manager: httpManager;

  constructor(httpManager: httpManager) {
    this.manager = httpManager;
   }

  getTutorProfile(id : number) : Observable<Tutor>
  {
    return this.manager.getTutorProfile(id);
  }
}
