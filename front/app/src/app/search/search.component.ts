import { Component, OnInit } from '@angular/core';
import { Tutor } from '../models/Tutor';
import { Subscription } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';
import { SearchService } from '../search.service';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit{
  
  searchString: string = '';
  results: Tutor[] = [];
  classPrefix: string = '';
  classNumber: string = '';
  tutorName: string = '';
  loading: boolean = false;
  noResults: boolean = false;

  private _subs : Subscription = new Subscription();

  constructor(
    private route : ActivatedRoute,
    private router : Router,
    private searchService : SearchService) {
      
   }
  
  ngOnInit(): void {
    this.loading = true;

    this.route.params.subscribe(params => {
      this.searchString = params['searchString'];
    });

    if(this.searchString == undefined)
    {
      this.loading = false;
      return;
    }
    this._subs.add(this.searchService.search(this.searchString).subscribe(res => {
      this.loading = false;
      this.results = res;
      console.log(this.results);
      if(this.results.length == 0 && this.searchString == undefined)
      {
        this.noResults = true;
      }
    }));
  }

  search() : void
  {
    if(this.classPrefix == '' && this.classNumber == '' && this.tutorName == '')
    {
      return;
    }
    this.searchString = this.classPrefix + "+" + this.classNumber + "+" + this.tutorName;
    this.router.navigate(['/search', this.searchString]);
  }

  toTutorProfile(id : number)
  {
    this.router.navigate(['/profile', id]);
  }

}
