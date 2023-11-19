import { Injectable } from '@angular/core';
import { Tutor } from './models/Tutor';
import { Observable, of } from 'rxjs';
import { httpManager } from './httpManager';
import { Student } from './models/Student';

@Injectable({
  providedIn: 'root'
})
export class ProfileService {

  manager: httpManager;

  constructor(httpManager: httpManager) {
    this.manager = httpManager;
   }

  getTutor(id : number) : Observable<Tutor>
  {
    return this.manager.getTutor(id);
  }

  getStudent(id : number) : Observable<Student>
  {
    return this.manager.getStudent(id);
  }

  getFavorites(id : number) : Observable<Tutor[]>
  {
    return this.manager.getFavorites(id);
  }

  isFavorited(studentId : number, tutorId : number) : Observable<boolean>
  {
    return this.manager.isFavorited(studentId, tutorId);
  }

  toggleFavorite(studentId : number, tutorId : number) : Observable<boolean>
  {
    return this.manager.toggleFavorite(studentId, tutorId);
  }
}
