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
import { Student } from './models/Student';


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
        return of(1);
    }

    studentLogin(user: StudentLoginRequest) : Observable<number>
    {
        //return this.http.post(this.backendUrl, user);
        return of(1);
    }

    getTutor(id: number) : Observable<Tutor>
    {
        //return this.http.get(this.backendUrl + '/' + id);
        return of(this.dummyTutor);
    }

    getStudent(id: number) : Observable<Student>
    {
        //return this.http.get(this.backendUrl + '/' + id);
        return of(this.dummyStudent);
    }


    dummyTutor : Tutor = {
        tutorId: 0,
        fullName: 'John Smith',
        courses: [
          'MATH 3163',
          'CS 4485',
          'CS 3377'
        ],
        totalHours: 20,
        available: true,
        profilePicture: new File(['assets/images/default.jpg'], 'profilePicture.jpg'),
        appointments: [
          {
            appointmentId: 0,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: "Sun Nov 05 2023.10:00 AM",
            subject: 'CS 3377'
          },
          {
            appointmentId: 1,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: "Wed Nov 08 2023.12:00 PM"
          },
          {
            appointmentId: 2,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: "Thu Nov 02 2023.11:00 AM",
            subject: 'MATH 3163'
          }
        ],
        tutorSchedule: [
          "Fri Oct 27 2023.10:00 AM",
          "Fri Oct 27 2023.11:00 AM",
          "Fri Oct 27 2023.01:00 PM",
          "Fri Oct 27 2023.12:00 PM",
          "Sat Oct 28 2023.10:00 AM",
          "Sat Oct 28 2023.01:00 PM",
          "Sat Oct 28 2023.11:00 AM",
          "Sat Oct 28 2023.12:00 PM",
          "Tue Oct 31 2023.10:00 AM",
          "Tue Oct 31 2023.11:00 AM",
          "Tue Oct 31 2023.02:00 PM",
          "Tue Oct 31 2023.09:00 AM",
          "Wed Nov 01 2023.10:00 AM",
          "Wed Nov 01 2023.08:00 AM",
          "Wed Nov 01 2023.09:00 AM",
          "Wed Nov 01 2023.12:00 PM",
          "Thu Nov 02 2023.10:00 AM",
          "Thu Nov 02 2023.11:00 AM",
          "Thu Nov 02 2023.12:00 PM",
          "Thu Nov 02 2023.01:00 PM",
          "Sat Nov 04 2023.10:00 AM",
          "Sat Nov 04 2023.11:00 AM",
          "Sat Nov 04 2023.12:00 PM",
          "Sat Nov 04 2023.01:00 PM",
          "Sun Nov 05 2023.10:00 AM",
          "Sun Nov 05 2023.11:00 AM",
          "Sun Nov 05 2023.12:00 PM",
          "Sun Nov 05 2023.01:00 PM",
          "Wed Nov 08 2023.10:00 AM",
          "Wed Nov 08 2023.11:00 AM",
          "Wed Nov 08 2023.12:00 PM",
          "Wed Nov 08 2023.01:00 PM",
        ]
    }

    dummyStudent : Student = {
      studentId : 0,
      fullName : 'Jane Doe',
      totalHours : 152,
      appointments : [
        {
          appointmentId: 0,
          studentId: 1,
          tutorId: 0,
          tutorName: 'John Smith',
          studentName: 'Jane Doe',
          time: "Sun Nov 05 2023.10:00 AM",
          subject: 'CS 3377'
        },
        {
          appointmentId: 1,
          studentId: 1,
          tutorId: 0,
          tutorName: 'John Smith',
          studentName: 'Jane Doe',
          time: "Wed Nov 08 2023.12:00 PM"
        },
        {
          appointmentId: 2,
          studentId: 1,
          tutorId: 0,
          tutorName: 'John Smith',
          studentName: 'Jane Doe',
          time: "Thu Nov 02 2023.11:00 AM",
          subject: 'MATH 3163'
        }
      ]
    }
}
