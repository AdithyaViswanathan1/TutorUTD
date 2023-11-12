import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthenticationService } from '../authentication.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-duo',
  templateUrl: './duo.component.html',
  styleUrls: ['./duo.component.scss']
})
export class DuoComponent implements OnInit{

  qrUrl: string = '';
  isStudent: boolean = false;


  constructor(
    private route : ActivatedRoute,
    private router : Router,
    private authService : AuthenticationService,
    private cookieService: CookieService
  ){
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    });
  }

  ngOnInit(): void {
    this.qrUrl = this.cookieService.get('duoQrUrl');
    //this.qrUrl = this.authService.getDuoQrUrl();
    if(this.qrUrl == undefined || this.qrUrl == '')
    {
      //this.router.navigate(['']);
    }
  }

  toLandingPage()
  {
    this.router.navigate(['']);
  }

  toLogin()
  {
    if(this.isStudent)
    {
      this.router.navigate(['/login', 'student']);
    }
    else
    {
      this.router.navigate(['/login', 'tutor']);
    }
  }

}
