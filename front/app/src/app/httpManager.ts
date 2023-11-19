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
import { LoginResponse } from './models/LoginResponse';
import { RegisterResponse } from './models/RegisterResponse';


@Injectable({
    providedIn: 'root'
})
export class httpManager {
    backendUrl : string = 'http://127.0.0.1:8000/';

    http: HttpClient;

    constructor(private httpClient: HttpClient) {
        this.http = httpClient;
    }

    tutorSignup(user: TutorSignupRequest) : Observable<RegisterResponse>
    {
        //todo: return http status code
        return this.http.post<RegisterResponse>(this.backendUrl + "login/tutor_register/", user)
    }

    tutorLogin(user: TutorLoginRequest) : Observable<LoginResponse>
    {
        return this.http.post<LoginResponse>(this.backendUrl + "login/tutor_login/", user);
    }

    studentSignup(user: StudentSignupRequest) : Observable<RegisterResponse>
    {
      return this.http.post<RegisterResponse>(this.backendUrl + "login/student_register/", user)
    }

    studentLogin(user: StudentLoginRequest) : Observable<LoginResponse>
    {
        return this.http.post<LoginResponse>(this.backendUrl + "login/student_login/", user);
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

    getFavorites(id: number) : Observable<Tutor[]>
    {
        //return this.http.get(this.backendUrl + '/' + id);
        let res = [this.dummyTutor];
        return of(res);
    }

    isFavorited(studentId: number, tutorId: number) : Observable<boolean>
    {
        //return this.http.get(this.backendUrl + '/' + id);
        return of(false);
    }

    toggleFavorite(studentId: number, tutorId: number) : Observable<boolean>
    {
        //return this.http.get(this.backendUrl + '/' + id);
        return of(true);
    }

    search(searchString : string) : Observable<Tutor[]>
    {
        //return this.http.get(this.backendUrl + '/' + searchString);
        let res = [this.dummyTutor];
        return of(res);
    }


    dummyTutor : Tutor = {
        tutorId: 0,
        fullName: 'John Smith',
        courses: [
          'MATH 3163',
          'CS 4485',
          'CS 3377',
          'CS 4398'
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
            time: "Sun Nov 19 2023.10:00 AM",
            subject: 'CS 3377'
          },
          {
            appointmentId: 1,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: "Wed Nov 15 2023.12:00 PM"
          },
          {
            appointmentId: 2,
            studentId: 1,
            tutorId: 0,
            tutorName: 'John Smith',
            studentName: 'Jane Doe',
            time: "Thu Nov 16 2023.11:00 AM",
            subject: 'MATH 3163'
          }
        ],
        tutorSchedule: [
          "Fri.10:00 AM",
          "Fri.11:00 AM",
          "Fri.01:00 PM",
          "Fri.12:00 PM",
          "Sat.10:00 AM",
          "Sat.01:00 PM",
          "Sat.11:00 AM",
          "Sat.12:00 PM",
          "Tue.10:00 AM",
          "Tue.11:00 AM",
          "Tue.02:00 PM",
          "Tue.09:00 AM",
          "Wed.10:00 AM",
          "Wed.08:00 AM",
          "Wed.09:00 AM",
          "Wed.12:00 PM",
          "Thu.10:00 AM",
          "Thu.11:00 AM",
          "Thu.12:00 PM",
          "Thu.01:00 PM",
          "Sat.10:00 AM",
          "Sat.11:00 AM",
          "Sat.12:00 PM",
          "Sat.01:00 PM",
          "Sun.10:00 AM",
          "Sun.11:00 AM",
          "Sun.12:00 PM",
          "Sun.01:00 PM"
        ],
        biography: "This is my biography!"
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
          time: "Sun Nov 19 2023.10:00 AM",
          subject: 'CS 3377'
        },
        {
          appointmentId: 1,
          studentId: 1,
          tutorId: 0,
          tutorName: 'John Smith',
          studentName: 'Jane Doe',
          time: "Wed Nov 15 2023.12:00 PM"
        },
        {
          appointmentId: 2,
          studentId: 1,
          tutorId: 0,
          tutorName: 'John Smith',
          studentName: 'Jane Doe',
          time: "Thu Nov 16 2023.11:00 AM",
          subject: 'MATH 3163'
        }
      ]
    }
}
