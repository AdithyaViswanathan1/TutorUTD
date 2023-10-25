import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { LoginRequest } from './models/LoginRequest';
import { SignUpRequest } from './models/SignUpRequest';
import { TutorSignupRequest } from './models/TutorSignupRequest';
import { TutorLoginRequest } from './models/TutorLoginRequest';
import { StudentSignupRequest } from './models/StudentSignupRequest';
import { StudentLoginRequest } from './models/StudentLoginRequest';
import { Observable, of } from 'rxjs';
import { Tutor } from './models/Tutor';


@Injectable({
    providedIn: 'root'
})
export class httpManager {
    backendUrl : string = 'https://example.com/api';

    http: HttpClient;

    constructor(private httpClient: HttpClient) {
        this.http = httpClient;
    }

    tutorSignup(user: TutorSignupRequest) : Observable<number>
    {
        //return this.http.post(this.backendUrl, user);
        return of(0);
    }

    tutorLogin(user: TutorLoginRequest) : Observable<number>
    {
        //return this.http.post(this.backendUrl, user);
        return of(0);
    }

    studentSignup(user: StudentSignupRequest) : Observable<number>
    {
        //return this.http.post(this.backendUrl, user);
        return of(0);
    }

    studentLogin(user: StudentLoginRequest) : Observable<number>
    {
        //return this.http.post(this.backendUrl, user);
        return of(0);
    }

    getTutorProfile(id: number) : Observable<Tutor>
    {
        //return this.http.get(this.backendUrl + '/' + id);
        return of(this.dummyTutor);
    }


    dummyTutor : Tutor = {
        tutorId: 0,
        firstName: 'John',
        lastName: 'Smith',
        courses: [
          {
            classPrefix: 'MATH',
            classNumber: 3163
          },
          {
            classPrefix: 'CS',
            classNumber: 4485
          },
          {
            classPrefix: 'CS',
            classNumber: 3377
          }
        ],
        appointments: [
          {
            appointmentId: 0,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: 'Wed Oct 25 2023.11:00 AM',
            subject: 'CS 3377'
          },
          {
            appointmentId: 1,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: 'Tue Oct 24 2023.10:30 AM'
          },
          {
            appointmentId: 2,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: 'Sat Oct 28 2023.11:00 AM',
            subject: 'MATH 3163'
          }
        ],
        tutorSchedule: [
          "Tue Oct 24 2023.10:30 AM",
          "Tue Oct 24 2023.11:00 AM",
          "Tue Oct 24 2023.11:30 AM",
          "Tue Oct 24 2023.12:00 PM",
          "Wed Oct 25 2023.10:30 AM",
          "Wed Oct 25 2023.11:00 AM",
          "Wed Oct 25 2023.11:30 AM",
          "Wed Oct 25 2023.12:00 PM",
          "Fri Oct 27 2023.10:30 AM",
          "Fri Oct 27 2023.11:00 AM",
          "Fri Oct 27 2023.11:30 AM",
          "Fri Oct 27 2023.12:00 PM",
          "Sat Oct 28 2023.10:30 AM",
          "Sat Oct 28 2023.11:00 AM",
          "Sat Oct 28 2023.11:30 AM",
          "Sat Oct 28 2023.12:00 PM",
          "Mon Oct 30 2023.10:30 AM",
          "Mon Oct 30 2023.11:00 AM",
          "Mon Oct 30 2023.11:30 AM",
          "Mon Oct 30 2023.12:00 PM",
        ]
      }
}