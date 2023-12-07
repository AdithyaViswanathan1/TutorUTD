import { Component, OnInit } from '@angular/core';
import { Tutor } from '../models/Tutor';
import { Subscription } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';
import { ProfileService } from '../profile.service';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-favorites',
  templateUrl: './favorites.component.html',
  styleUrls: ['./favorites.component.scss']
})
export class FavoritesComponent implements OnInit {
  
  favorites: Tutor[] = [];
  studentId: number = 0;
  loading: boolean = false;
  noFavorites: boolean = false;

  private _subs : Subscription = new Subscription();

  constructor(
    private profileService: ProfileService,
    private router : Router,
    private cookieService: CookieService
  ) {}


  ngOnInit(): void {
    this.studentId = parseInt(this.cookieService.get('userId'));
    this.loading = true;
    this._subs.add(this.profileService.getFavorites(this.studentId).subscribe(favorites => {
      this.loading = false;
      this.favorites = favorites;
      if(this.favorites.length == 0)
      {
        this.noFavorites = true;
      }
    }));
  }

  toTutorProfile(id : number)
  {
    this.router.navigate(['/profile', id]);
  }
}
