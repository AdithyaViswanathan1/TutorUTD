import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.scss']
})
export class SignUpComponent {
  isStudent: boolean = true;

  constructor(private route : ActivatedRoute) {
    this.route.params.subscribe(params => {
      this.isStudent = params['userType'] == 'student';
    });
  }

}
