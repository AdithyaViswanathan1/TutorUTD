import { Component, OnInit } from '@angular/core';
import { Tutor } from '../models/Tutor';
import { Subscription } from 'rxjs';
import { ActivatedRoute, Router } from '@angular/router';
import { SearchService } from '../search.service';
import { SearchInput } from '../models/SearchInput';
import { SearchResult } from '../models/SearchResult';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss']
})
export class SearchComponent implements OnInit{
  
  searchString: string = '';
  results: SearchResult[] = [];
  classPrefix: string = '';
  classNumber: string = '';
  tutorName: string = '';
  searchInput: SearchInput = {course_prefix: '', course_number: '', tutor_name: ''};
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

    this.searchInput.course_prefix = this.searchString.split('+')[0];
    this.searchInput.course_number = this.searchString.split('+')[1];
    this.searchInput.tutor_name = this.searchString.split('+')[2];

    this._subs.add(this.searchService.search(this.searchInput).subscribe(res => {
      this.loading = false;
      this.results = res;
      console.log(res);
      if(this.results.length == 0 && this.searchString == undefined)
      {
        this.noResults = true;
      }
    }));
  }

  search() : void
  {
    this.searchString = this.classPrefix + "+" + this.classNumber + "+" + this.tutorName;
    this.router.navigate(['/search', this.searchString]);
  }

  toTutorProfile(id : number)
  {
    this.router.navigate(['/profile', id]);
  }

}
