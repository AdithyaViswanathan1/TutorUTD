import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Subscription } from 'rxjs';
import { ProfileService } from '../../profile.service';
import { ProfileEdit } from 'src/app/models/ProfileEdit';

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.scss']
})
export class EditProfileComponent {
  @Input() input: ProfileEdit = {fullName: '', biography: '', courses: []};

  @Output() close = new EventEmitter();
  @Output() save = new EventEmitter<ProfileEdit>();

  private _subs : Subscription = new Subscription();

  name: string = '';
  bio: string = '';
  courses: string[] = [];

  addCourse: boolean = false;
  newCourse: string = "";

  constructor(private profileService: ProfileService) { 
  }

  ngOnInit(): void {
    this.name=this.input.fullName || "";
    this.bio=this.input.biography || "";
    this.courses=this.input.courses || [];
  }

  cancelChanges()
  {
    this.close.emit();
  }

  saveChanges()
  {
    let out : ProfileEdit = {
      fullName: this.name, 
      biography: this.bio, 
      courses: this.courses
    };
    this.save.emit(out);
  }

  addCourseToList(){
    this.courses.push(this.newCourse);
    this.newCourse = "";
  }

  removeCourse(course: string){
    const courseToRemove = this.courses.indexOf(course);
    if(courseToRemove !== -1){
      this.courses.splice(courseToRemove, 1);
    }
  }

}
