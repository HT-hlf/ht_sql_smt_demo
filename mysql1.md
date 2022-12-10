```mysql
CREATE Function birthday(sage date)
returns boolean NOT DETERMINISTIC NO SQL
begin
   declare date_now date;
   declare bool boolean;
   set date_now = curdate();
   if month(sage)=12 and month(date_now)=1 then
      if week(replace(sage, year(sage), year(date_now)-1), 7) = week(date_now,7) then
         set bool = 1;
      else
         set bool = 0;
      end if;
   elseif month(date_now)=12 and month(sage)=1 then
      if week(replace(sage, year(sage), year(date_now)+1), 7) = week(date_now,7) then
         set bool = 1;
      else
         set bool = 0;
      end if;
   elseif month(sage)=2 and day(sage)=29 then
      if year(date_now)%4=0 then
         if week(replace(sage, year(sage), year(date_now)),7) = week(date_now,7) then
	    set bool = 1;
         else
	    set bool = 0;
         end if;
      else
         if week(concat_ws('-',year(curdate()),'03','01'),7) = week(date_now,7) then
	    set bool = 1;
         else
	    set bool = 0;
         end if;
      end if;
   else
      if week(replace(sage, year(sage), year(date_now)),7) = week(date_now,7) then
         set bool = 1;
      else
         set bool = 0;
      end if;
   end if;
   return bool;
end
```

