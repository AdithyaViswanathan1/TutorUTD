import { Injectable } from '@angular/core';
import { httpManager } from './httpManager';
import { Observable, of } from 'rxjs';
import { SearchInput } from './models/SearchInput';
import { SearchResult } from './models/SearchResult';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private httpManager: httpManager) {
   }

  search(input : SearchInput) : Observable<SearchResult[]>
  {
    return this.httpManager.search(input);
  }
}
