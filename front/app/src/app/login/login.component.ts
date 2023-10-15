import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  isStudent: boolean = true;

  constructor(private route : ActivatedRoute) {
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    });
  }


}
