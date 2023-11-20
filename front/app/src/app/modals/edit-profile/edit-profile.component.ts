import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Subscription } from 'rxjs';
import { ProfileService } from '../../profile.service';

@Component({
  selector: 'app-edit-profile',
  templateUrl: './edit-profile.component.html',
  styleUrls: ['./edit-profile.component.scss']
})
export class EditProfileComponent {
  @Input() courses: string[] = [];

  @Output() cancel = new EventEmitter<number>();
  @Output() close = new EventEmitter();
  @Output() name = new EventEmitter<string>();
  @Output() bio = new EventEmitter<string>();

  private _subs : Subscription = new Subscription();

  nameInput: string = '';
  bioInput: string = '';

  addCourse: boolean = false;
  newCourse: string = "";

  tutorId: number = 0;

  constructor(private profileService: ProfileService) { 
  }

  ngOnInit(): void {
    this._subs.add(this.profileService.getTutor(this.tutorId).subscribe(tutor => {
      this.nameInput = tutor.full_name;
      this.bioInput = tutor.biography;
    }));
  }

  cancelChanges()
  {
    this.close.emit();
  }

  saveChanges()
  {
    this.name.emit(this.nameInput);
    this.bio.emit(this.bioInput);
    this.close.emit();
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
